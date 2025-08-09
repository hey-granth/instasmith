from google import genai
from app.core.config import Config
from app.core.logger import logger


def generate_caption(topic: str, tone: str = 'professional', max_length: int = 200) -> str:
    if not Config.GEMINI_API_KEY:
        logger.warning("No gemini api key")
        raise RuntimeError("GEMINI_API_KEY not set")

    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    prompt: str = (
        f"Generate a {tone} caption for the topic: '{topic}'. "
        f"The caption should be concise, engaging, and suitable for social media. "
        f"Limit the caption to {max_length} characters."
    )

    try:
        logger.info(f"Generating caption for topic: {topic}, tone: {tone}, max_length: {max_length}")
        response = client.models.generate_content(model=Config.GEMINI_MODEL, contents=prompt)
        return str(response.text).strip()

    except Exception as e:
        logger.exception("No caption generated")
        raise RuntimeError(f"Failed to generate caption: {e}")