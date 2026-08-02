(function () {
  var root = document.getElementById("nav-root");
  if (!root) return;
  var current = (root.getAttribute("data-current") || "").replace(/^\/+/, "");

  function el(tag, cls) { var e = document.createElement(tag); if (cls) e.className = cls; return e; }

  // collect the set of out-paths on the trail to `current`
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

  fetch("/assets/nav.json").then(function (r) { return r.json(); }).then(function (nav) {
    var trail = findTrail(nav, current, []) || [];
    var trailOuts = {};
    trail.forEach(function (n) { if (n.out) trailOuts[n.out] = true; });

    function render(nodes) {
      var ul = el("ul", "nav-list");
      nodes.forEach(function (n) {
        var li = el("li", "nav-item");
        var hasKids = n.children && n.children.length;
        var isActive = n.out && n.out === current;
        var link = n.out ? "/" + n.out : null;

        if (hasKids) {
          var det = el("details");
          if (trailOuts[n.out] || isActive) det.open = true;
          var sum = el("summary");
          if (link) {
            var a = el("a"); a.href = link; a.textContent = n.title;
            if (isActive) a.className = "active-link";
            sum.appendChild(a);
          } else {
            var sp = el("span", "nav-label"); sp.textContent = n.title; sum.appendChild(sp);
          }
          det.appendChild(sum);
          det.appendChild(render(n.children));
          li.appendChild(det);
        } else if (link) {
          var a2 = el("a"); a2.href = link; a2.textContent = n.title;
          if (isActive) { li.className = "nav-item active"; }
          li.appendChild(a2);
        } else {
          var sp2 = el("span", "nav-label"); sp2.textContent = n.title; li.appendChild(sp2);
        }
        ul.appendChild(li);
      });
      return ul;
    }

    root.appendChild(render(nav));
    var act = root.querySelector(".active-link, .nav-item.active > a");
    if (act && act.scrollIntoView) act.scrollIntoView({ block: "center" });
  }).catch(function (e) {
    root.textContent = "navigation failed to load";
  });
})();
