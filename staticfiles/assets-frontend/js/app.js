var dyingearth = dyingearth || {};
jQuery(function ($) {
  "use strict";

  //preloader
  $(window).ready(function () {
    $("#preloader").delay(100).fadeOut("fade");
  });


  //sticky header
  $(window).on("scroll", function () {
    var scroll = $(window).scrollTop();
    if (scroll < 2) {
      $("nav.sticky-header").removeClass("affix");
    } else {
      $("nav.sticky-header").addClass("affix");
    }
  });


  
  // dark light mood
  var setDarkMode = (active = false) => {
    var wrapper = document.querySelector(":root");
    if (active) {
      wrapper.setAttribute("data-bs-theme", "dark");
      localStorage.setItem("theme", "dark");
    } else {
      wrapper.setAttribute("data-bs-theme", "light");
      localStorage.setItem("theme", "light");
    }
  };
  var toggleDarkMode = () => {
    var theme = document.querySelector(":root").getAttribute("data-bs-theme");
    // If the current theme is "light", we want to activate dark
    setDarkMode(theme === "light");
  };
  var initDarkMode = () => {
    var theme = localStorage.getItem("theme");
    if (theme == "dark") {
      setDarkMode(true);
    } else {
      setDarkMode(false);
    }
    var toggleButton = document.querySelector(".tt-theme-toggle");
    toggleButton && toggleButton.addEventListener("click", toggleDarkMode);
  };
  initDarkMode();
});