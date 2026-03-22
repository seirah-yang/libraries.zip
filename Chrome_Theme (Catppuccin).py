@-moz-document regexp("Chrome_Theme (Catppuccin).*") {
/* =========================
   macOS Global Readability
   ========================= */

html, body {
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Noto Sans KR", sans-serif !important;
  line-height: 1.62 !important;
  letter-spacing: 0.15px !important;
  text-rendering: optimizeLegibility !important;
  -webkit-font-smoothing: antialiased !important;
  -moz-osx-font-smoothing: grayscale !important;
}

body {
  background-color: #1e1e2e !important;
  color: #cdd6f4 !important;
}

a {
  color: #89b4fa !important;
}

/* 일반 텍스트 */
p, li, dd, dt, span, div, article, section, main, aside, blockquote {
  line-height: 1.62 !important;
}

/* 제목은 너무 무겁지 않게 */
h1, h2, h3, h4, h5, h6 {
  line-height: 1.35 !important;
  letter-spacing: 0.05px !important;
}

/* 입력창 */
input, textarea, select, button {
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Noto Sans KR", sans-serif !important;
  line-height: 1.45 !important;
}

/* 코드/숫자/표 */
code, pre, kbd, samp,
table, th, td {
  font-family: "JetBrains Mono", "SFMono-Regular", Menlo, Monaco, Consolas, monospace !important;
  font-variant-numeric: tabular-nums slashed-zero !important;
}

/* 코드 블록 */
code, pre, kbd, samp {
  font-size: 0.95em !important;
  line-height: 1.55 !important;
}

/* 표 가독성 */
table {
  border-collapse: collapse !important;
}

th, td {
  line-height: 1.5 !important;
  vertical-align: middle !important;
}

/* 숫자 필드 */
input[type="number"] {
  font-family: "JetBrains Mono", "SFMono-Regular", Menlo, Monaco, Consolas, monospace !important;
  font-variant-numeric: tabular-nums slashed-zero !important;
}

/* 링크 가독성 */
a {
  text-underline-offset: 0.12em !important;
}

/* 작은 글씨/주석 */
small, .text-xs, .text-sm {
  line-height: 1.5 !important;
}

/* 지나치게 얇은 폰트 보정 */
* {
  font-weight: normal;
}
}
