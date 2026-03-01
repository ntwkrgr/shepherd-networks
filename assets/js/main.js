document.addEventListener("DOMContentLoaded", function () {
  if (window.lucide) { lucide.createIcons(); }

  var header = document.getElementById("site-header");
  var toggle = document.querySelector(".nav-toggle");
  var navLinks = document.getElementById("nav-links");
  var navLinkEls = document.querySelectorAll(".nav-link");

  // ── Hamburger toggle ──────────────────────────────────────
  if (toggle && navLinks) {
    toggle.addEventListener("click", function () {
      var isOpen = navLinks.classList.toggle("open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });

    // Close menu when a nav link is clicked
    navLinks.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        navLinks.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // ── Header shadow on scroll ───────────────────────────────
  if (header) {
    window.addEventListener("scroll", function () {
      if (window.scrollY > 20) {
        header.classList.add("scrolled");
      } else {
        header.classList.remove("scrolled");
      }
    }, { passive: true });
  }

  // ── Active nav link via IntersectionObserver ──────────────
  var sections = document.querySelectorAll("section[id]");
  if (sections.length && navLinkEls.length) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            var id = entry.target.getAttribute("id");
            navLinkEls.forEach(function (link) {
              link.classList.toggle("active", link.getAttribute("data-section") === id);
            });
          }
        });
      },
      {
        rootMargin: "-30% 0px -60% 0px",
        threshold: 0
      }
    );

    sections.forEach(function (section) {
      observer.observe(section);
    });
  }

  // ── Smooth scroll polyfill for anchor links ───────────────
  // (Most modern browsers support scroll-behavior: smooth in CSS,
  //  but this ensures the header offset is respected for JS clicks)
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener("click", function (e) {
      var targetId = anchor.getAttribute("href").slice(1);
      var target = document.getElementById(targetId);
      if (target) {
        e.preventDefault();
        var headerH = header ? header.offsetHeight : 0;
        var top = target.getBoundingClientRect().top + window.scrollY - headerH;
        window.scrollTo({ top: top, behavior: "smooth" });
      }
    });
  });
});
