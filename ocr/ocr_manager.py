import os
from dotenv import load_dotenv
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

class OCRManager:
    def __init__(self):
        load_dotenv()
        ai_endpoint = os.getenv("AI_SERVICE_ENDPOINT")
        ai_key = os.getenv("AI_SERVICE_KEY")

        self._ocr = ImageAnalysisClient(
            endpoint=ai_endpoint,
            credential=AzureKeyCredential(ai_key)
        )

    def extract_text(self, image_path: str) -> str:
        texts = []
        with open(f'{image_path}.jpg', "rb") as f:
            image_data = f.read()

        result = self._ocr.analyze(
            image_data=image_data,
            visual_features=[VisualFeatures.READ]
        )

        if result.read is not None:
            for block in result.read.blocks:
                for line in block.lines:
                    text = line.text.strip()
                    texts.append(text)

        return "\n".join(texts)