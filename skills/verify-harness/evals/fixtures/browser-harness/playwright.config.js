import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
  use: {
    baseURL: "http://127.0.0.1:4178",
    browserName: "chromium",
  },
  webServer: {
    command: "node server.mjs",
    url: "http://127.0.0.1:4178",
    reuseExistingServer: false,
  },
});
