from pyyoutube import Client
import pyyoutube.models as mds
from pyyoutube.media import Media
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.config import app_config
from app.infrastructure.google_service import refresh_access_token, get_tokens, device_authorization
from app.use_cases.token.update_token_case import UpdateTokenCase


class YoutubeUpload:
    def __init__(self, db: AsyncSession, access_token, refresh_token):
        self.client = Client(access_token=access_token)
        self.update_token_use_case = UpdateTokenCase(db)
        self.refresh_token = refresh_token

    async def check_token_validity(self):

        """
        Проверка действительности access_token через YouTube API.
        """
        try:
            response = self.client.channels.list(part="id", mine=True)
            if response.items:
                print("Токен действителен.")
                return True
        except Exception as e:
            if "401" in str(e):
                print("Токен недействителен. Обновление токена...")
                try:
                    access_token = refresh_access_token(
                        client_id=app_config.google_client_id,
                        client_secret=app_config.google_secret,
                        refresh_token=self.refresh_token
                    )
                    self.client = Client(access_token=access_token)
                    await self.update_token_use_case.execute(access_token=access_token)
                    print("Токен успешно обновлён.")
                    return True
                except Exception as e:
                    print("Ошибка при обращении к Google API:", e)
                    return False
            else:
                print("Произошла ошибка при проверке токена:", e)
                return False

    async def upload_video(self, file_path, title, description, category_id="27", notify_subscribers=True):
        try:
            if not await self.check_token_validity():
                print("Не удалось проверить токен. Загрузка видео невозможна.")
                result = get_tokens(client_id=app_config.google_client_id)
                return result

            # Подготовка тела запроса
            body = mds.Video(
                snippet=mds.VideoSnippet(
                    title=title,
                    description=description,
                    categoryId=category_id
                ),
                status=mds.VideoStatus(
                    privacyStatus="private"  # Устанавливаем приватный статус
                )
            )

            # Создание объекта медиа
            media = Media(filename=file_path)

            # Инициализация загрузки
            upload = self.client.videos.insert(
                body=body,
                media=media,
                parts=["snippet", "status"],
                notify_subscribers=notify_subscribers
            )

            video_body = None
            while video_body is None:
                status, video_body = upload.next_chunk()
                if status:
                    print(f"Прогресс загрузки: {status.progress() * 100:.2f}%")

            print("Видео успешно загружено!", video_body)
            return video_body

        except Exception as e:
            print("Произошла ошибка при загрузке видео:", e)
            return None
