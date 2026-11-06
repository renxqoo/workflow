import { expect, test } from "@playwright/test";

test("retired home path redirects to the root", async ({ page }) => {
  await page.goto("/home-v2");
  await expect(page).toHaveURL("/");
});
