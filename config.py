"""不動産投資コンパス - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "不動産投資コンパス"
BLOG_DESCRIPTION = "不動産投資・賃貸経営の基礎から実践まで。区分マンション・一棟アパート・REIT・新築/中古の比較、融資・税金・出口戦略を体系的に学べる。"
BLOG_URL = "https://musclelove-777.github.io/fudosan-compass/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/fudosan-compass"

TARGET_CATEGORIES = [
    "不動産投資の基礎",
    "物件選びと立地分析",
    "融資・ローン戦略",
    "税金・確定申告",
    "賃貸経営・管理",
    "リスク対策",
    "出口戦略・売却",
    "REIT・小口投資",
]

THEME = {
    "primary": "#1e3a5f",
    "accent": "#d4a55a",
    "gradient_start": "#1e3a5f",
    "gradient_end": "#d4a55a",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
