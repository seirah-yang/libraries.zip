@-moz-document regexp(".*") {

/* =========================
   Windows Global Readability
   ========================= */

html, body {
  font-family: Inter, "Segoe UI", "Malgun Gothic", "Noto Sans KR", sans-serif !important;
  line-height: 1.64 !important;
  letter-spacing: 0.18px !important;
  text-rendering: optimizeLegibility !important;
  -webkit-font-smoothing: antialiased !important;
}

/* 일반 텍스트 */
p, li, dd, dt, span, div, article, section, main, aside, blockquote {
  line-height: 1.64 !important;
}

/* 제목 */
h1, h2, h3, h4, h5, h6 {
  line-height: 1.36 !important;
  letter-spacing: 0.04px !important;
  font-weight: 600 !important;
}

body {
  background-color: #1e1e2e !important;
  color: #cdd6f4 !important;
}

a {
  color: #89b4fa !important;
}

/* 입력창 */
input, textarea, select, button {
  font-family: Inter, "Segoe UI", "Malgun Gothic", "Noto Sans KR", sans-serif !important;
  line-height: 1.45 !important;
}

/* 코드/숫자/표 */
code, pre, kbd, samp,
table, th, td {
  font-family: "JetBrains Mono", Consolas, "Cascadia Mono", monospace !important;
  font-variant-numeric: tabular-nums slashed-zero !important;
}

/* 코드 블록 */
code, pre, kbd, samp {
  font-size: 0.95em !important;
  line-height: 1.56 !important;
}

/* 표 */
table {
  border-collapse: collapse !important;
}

th, td {
  line-height: 1.52 !important;
  vertical-align: middle !important;
}

/* 숫자 입력 */
input[type="number"] {
  font-family: "JetBrains Mono", Consolas, "Cascadia Mono", monospace !important;
  font-variant-numeric: tabular-nums slashed-zero !important;
}

/* 링크 */
a {
  text-underline-offset: 0.12em !important;
}

/* 작은 글씨 */
small, .text-xs, .text-sm {
  line-height: 1.5 !important;
}

/* 너무 가는 렌더링 보정 */
body, p, li, td, th, input, textarea, select, button {
  font-weight: 400 !important;
}

}
