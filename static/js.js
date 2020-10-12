const input = document.querySelector("input");
const label = document.querySelector("label");

input.addEventListener("input", event => {
  const value = Number(input.value) / 100;
  label.innerHTML = Math.round(value * 100);
});