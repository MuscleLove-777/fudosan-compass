"""不動産投資コンパス - プロンプト定義"""


def build_keyword_prompt(config):
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    return (
        f"{config.BLOG_NAME}用のキーワードを選定してください。\n\n"
        "以下のカテゴリから1つ選び、そのカテゴリで検索需要が高いキーワードを1つ提案してください。\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        "【キーワード選定の基準】\n"
        "- ロングテールキーワード（3語以上の組み合わせ）を優先\n"
        "- 比較系・疑問系・体験系を意識\n"
        "- 季節性・トレンドも考慮\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    return f"""あなたは宅建士資格を持ち、複数の収益物件を運営する実践派の不動産投資家です。

【依頼】
キーワード「{keyword}」（カテゴリ: {category}）について、
{config.BLOG_NAME}で公開する SEO最適化された日本語ブログ記事を1本生成してください。

【記事方針】
- 利回り・キャッシュフローなどの数字を具体的に示す
- リスク（空室・修繕・金利上昇）も同等の比重で記述
- 税制（青色申告・減価償却・損益通算）に踏み込む
- 「絶対儲かる」系の煽り表現は厳禁、シミュレーションベースで

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること（32文字以内）
2. H2見出しを4〜6個、必要に応じてH3も使用
3. メタディスクリプションは120文字以内
4. 内部リンクのプレースホルダーを2〜3箇所配置（{{{internal_link:関連トピック}}}）
5. 各H2見出しの先頭に絵文字（例: ## 🔍 〜）

【ビジュアル要件】
- 比較表・ステップ表をMarkdownテーブルで積極使用
- 「💡 ポイント」「⚠️ 注意」「✅ まとめ」を引用ブロック（>）で配置
- 各H2セクション間に画像プレースホルダー {{{content_image}}}（合計3〜5箇所）

【出力形式】
以下のJSON形式のみで出力（コードフェンスなし、説明文なし）:

{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "hero_emoji": "🚀",
  "hero_gradient": "135deg",
  "image_search_query": "english keywords for image",
  "content_image_count": 4
}}

【厳守事項】
- 文字数 {config.MAX_ARTICLE_LENGTH}文字程度
- tagsは5個ちょうど
- slugは半角英数字とハイフンのみ
- contentはMarkdownエスケープ済みのJSON文字列として有効に
"""
