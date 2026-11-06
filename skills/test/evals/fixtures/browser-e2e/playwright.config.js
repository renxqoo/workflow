import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
  use: {
    baseURL: "http://127.0.0.1:4177",
    browserName: "chromium",
  },
  webServer: {
    command: "node server.mjs",
    url: "http://127.0.0.1:4177",
    reuseExistingServer: false,
  },
});
