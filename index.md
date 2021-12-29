---
layout: home
title: Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }} 📊
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

<p style="color:red">Looking for the Fall 2021 site? <a style="color:red" href="https://dsc-courses.github.io/dsc10-2021-fa">Click here</a>.</p>

{{ site.staffersnobio }}

[Lecture Zoom Link](https://ucsd.zoom.us/my/rampure){: .btn .btn-blue } [Recordings](https://www.youtube.com/playlist?list=PLDNbnocpJUhZDpPKmmbgXAuZqYYPhC0D-){: .btn .btn-green }

**Note:** Until this disclaimer is removed, all information at this site should be treated as temporary and subject to change.

{% for module in site.modules %}
{{ module }}
{% endfor %}