import { createServer } from "node:http";

function catalogPage(unavailable) {
  if (unavailable) {
    return `<h1>Model catalog</h1><p role="status">Catalog temporarily unavailable</p><button>All</button>`;
  }

  return `<h1>Model catalog</h1>
    <div class="filters">
      <button data-filter="All">All</button>
      <button data-filter="Text">Text</button>
      <button data-filter="Image">Image</button>
      <button data-filter="Video">Video</button>
    </div>
    <div class="catalog-grid">
      <a data-category="Text" href="/models/aurora">Open Aurora</a>
      <a data-category="Image" href="/models/pixel">Open Pixel</a>
      <a data-category="Video" href="/models/motion">Open Motion</a>
    </div>`;
}

function pageContent(pathname, unavailable) {
  if (pathname === "/catalog") return catalogPage(unavailable);
  if (pathname === "/models/aurora") return "<h1>Aurora model</h1>";
  if (pathname === "/models/pixel") return "<h1>Pixel model</h1>";
  if (pathname === "/models/motion") return "<h1>Motion model</h1>";
  if (pathname === "/home-v2") return "<h1>Retired page</h1>";
  return "<h1>Welcome</h1>";
}

function document(pathname, unavailable) {
  return `<!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
          .menu-toggle { display: none; }
          .catalog-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
          [hidden] { display: none !important; }
          @media (max-width: 600px) {
            .menu-toggle { display: inline-block; }
            .catalog-grid { grid-template-columns: 1fr; }
          }
        </style>
      </head>
      <body>
        <button class="menu-toggle" id="open-menu">Open menu</button>
        <nav aria-label="Mobile menu" id="mobile-menu" hidden>
          <button id="close-menu">Close menu</button>
          <a href="/catalog">Catalog</a>
        </nav>
        <main>${pageContent(pathname, unavailable)}</main>
        <script>
          const openButton = document.getElementById("open-menu");
          const closeButton = document.getElementById("close-menu");
          const menu = document.getElementById("mobile-menu");
          openButton.addEventListener("click", () => { menu.hidden = false; });
          closeButton.addEventListener("click", () => {
            menu.hidden = true;
            openButton.focus();
          });
          for (const button of document.querySelectorAll("[data-filter]")) {
            button.addEventListener("click", () => {
              const category = button.dataset.filter;
              for (const card of document.querySelectorAll("[data-category]")) {
                card.hidden = category !== "All" && card.dataset.category !== category;
              }
            });
          }
        </script>
      </body>
    </html>`;
}

createServer((request, response) => {
  const url = new URL(request.url, "http://127.0.0.1:4177");
  response.writeHead(200, { "content-type": "text/html; charset=utf-8" });
  response.end(document(url.pathname, url.searchParams.get("cms") === "down"));
}).listen(4177, "127.0.0.1");
