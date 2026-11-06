import { expect, test } from "@playwright/test";

test("catalog cards open model details", async ({ page }) => {
  await page.goto("/catalog");
  await page.getByRole("link", { name: "Open Aurora" }).click();
  await expect(page.getByRole("heading", { name: "Aurora model" })).toBeVisible();
});

test("catalog filters published models", async ({ page }) => {
  await page.goto("/catalog");
  await page.getByRole("button", { name: "Image" }).click();
  await expect(page.getByRole("link", { name: "Open Pixel" })).toBeVisible();
  await expect(page.getByRole("link", { name: "Open Aurora" })).toBeHidden();
});

test("catalog keeps every category during a content outage", async ({ page }) => {
  await page.goto("/catalog?cms=down");
  await expect(page.getByRole("button", { name: "Image" })).toBeVisible();
});

test("catalog uses three columns at 1440px", async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto("/catalog");
  const columns = await page.locator(".catalog-grid").evaluate((element) =>
    getComputedStyle(element).gridTemplateColumns.split(" ").length,
  );
  expect(columns).toBe(3);
});
