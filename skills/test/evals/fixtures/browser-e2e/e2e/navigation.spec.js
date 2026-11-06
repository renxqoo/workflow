import { expect, test } from "@playwright/test";

test.use({ viewport: { width: 390, height: 844 } });

test("mobile menu opens with keyboard focus inside", async ({ page }) => {
  await page.goto("/");
  await page.getByRole("button", { name: "Open menu" }).click();
  await expect
    .poll(() =>
      page
        .getByRole("navigation", { name: "Mobile menu" })
        .evaluate((menu) => menu.contains(document.activeElement)),
    )
    .toBe(true);
  await page.getByRole("button", { name: "Close menu" }).click();
  await expect(page.getByRole("button", { name: "Open menu" })).toBeFocused();
});

test("mobile menu navigates to the catalog", async ({ page }) => {
  await page.goto("/");
  await page.getByRole("button", { name: "Open menu" }).click();
  await page.getByRole("link", { name: "Catalog" }).click();
  await expect(page.getByRole("heading", { name: "Model catalog" })).toBeVisible();
});
