(function () {
  var root = document.getElementById("nav-root");
  if (!root) return;
  var current = (root.getAttribute("data-current") || "").replace(/^\/+/, "");
  var base = root.getAttribute("data-root") || ".";

  function href(out) { return base + "/" + out; }
  function el(tag, cls) { var e = document.createElement(tag); if (cls) e.className = cls; return e; }

  function findTrail(nodes, target, acc) {
    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i];
      var here = acc.concat([n]);
      if (n.out && n.out === target) return here;
      if (n.children && n.children.length) {
        var r = findTrail(n.children, target, here);
        if (r) return r;
      }
    }
    return null;
  }

  fetch(base + "/assets/nav.json").then(function (r) { return r.json(); }).then(function (nav) {
    var trail = findTrail(nav, current, []) || [];
    var trailOuts = {};
    trail.forEach(function (n) { if (n.out) trailOuts[n.out] = true; });

    function render(nodes) {
      var ul = el("ul", "nav-list");
      nodes.forEach(function (n) {
        var li = el("li", "nav-item");
        var hasKids = n.children && n.children.length;
        var isActive = n.out && n.out === current;

        if (hasKids) {
          var det = el("details");
          if (trailOuts[n.out] || isActive) det.open = true;
          var sum = el("summary");
          var a = el("a");
          a.href = href(n.out); a.textContent = n.title;
          if (isActive) a.className = "active-link";
          sum.appendChild(a);
          det.appendChild(sum);
          det.appendChild(render(n.children));
          li.appendChild(det);
        } else {
          var a2 = el("a");
          a2.href = href(n.out); a2.textContent = n.title;
          if (isActive) li.className = "nav-item active";
          li.appendChild(a2);
        }
        ul.appendChild(li);
      });
      return ul;
    }

    root.appendChild(render(nav));
    var act = root.querySelector(".active-link, .nav-item.active > a");
    if (act && act.scrollIntoView) act.scrollIntoView({ block: "center" });

    // filter box
    var box = document.createElement("input");
    box.type = "search"; box.className = "nav-filter"; box.placeholder = "Filter pages…";
    root.parentNode.insertBefore(box, root);
    box.addEventListener("input", function () {
      var q = box.value.trim().toLowerCase();
      root.querySelectorAll(".nav-item").forEach(function (li) {
        var a = li.querySelector("a");
        var hit = !q || (a && a.textContent.toLowerCase().indexOf(q) !== -1);
        if (hit) {
          li.classList.remove("nav-hidden");
          for (var p = li.parentNode; p && p !== root; p = p.parentNode) {
            if (p.classList && p.classList.contains("nav-item")) p.classList.remove("nav-hidden");
            if (p.tagName === "DETAILS" && q) p.open = true;
          }
        } else if (!li.querySelector(".nav-item:not(.nav-hidden)")) {
          li.classList.add("nav-hidden");
        }
      });
      if (!q) root.querySelectorAll("details").forEach(function (d) {
        d.open = !!(d.querySelector(".active-link") || trailOuts[current]) && d.contains(act);
      });
    });
  }).catch(function () {
    root.textContent = "navigation failed to load";
  });
})();
