const doc = document;
let sidebarButton = doc.querySelector(".menu-btn");
let sidebar = doc.querySelector(".sidebar");

sidebarButton.addEventListener("click", () => {
  sidebar.classList.toggle('sidebar-opened');
});
