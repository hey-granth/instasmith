from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
from app.services.caption_service import generate_caption
from app.services.image_service import generate_image
from app.services.instagram_service import upload_photo
from app.services.storage_service import upload_with_rclone
from app.api.schemas import CaptionRequest, ImageRequest, PostRequest
from app.core.logger import logger


router = APIRouter()


@router.get("/ping")
async def ping():
    return {"message": "pong"}


@router.get("/generate-caption")
async def generate_caption_route(body: CaptionRequest):
    try:
        caption = generate_caption(body.topic, body.tone or "professional")
        return JSONResponse({"caption": caption})
    except Exception as e:
        logger.exception(f'Error generating caption: {e}')
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/generate-image")
async def generate_image_route(body: ImageRequest):
    try:
        path = generate_image(body.prompt)
        return JSONResponse({"image_path": path})
    except Exception as e:
        logger.exception(f'Error generating image: {e}')
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/post")
async def post_route(body: PostRequest):
    try:
        prompt: str = body.prompt or body.topic
        caption: str = generate_caption(body.topic, body.tone or "professional")
        image_path: str = generate_image(prompt)
        rclone_path: str = ''
        insta_response: dict = upload_photo(image_path, caption)
        if upload_with_rclone and upload_with_rclone.__name__:
            if __import__('os').getenv('USE_RCLONE', 'false').lower() == 'true':
                logger.info('Uploading image with rclone...')
                rclone_path = upload_with_rclone(image_path)
            else:
                logger.info('Not using rclone for image upload...')

        return JSONResponse({"caption": caption, "image_path": image_path, "rclone_path": rclone_path, "insta_response": insta_response})

    except Exception as e:
        logger.exception(f'Error creating post: {e}')
        raise HTTPException(status_code=500, detail=str(e))