class FyproSocialBuyerClient:
    def check_comment(self, user_comment: str, product_sku: str) -> dict:
        trigger = "buy" in user_comment.lower() or "price" in user_comment.lower()
        url = f"https://nile.shop/checkout/{product_sku}?ref=fypro" if trigger else ""
        return {"trigger_dm": trigger, "checkout_url": url}