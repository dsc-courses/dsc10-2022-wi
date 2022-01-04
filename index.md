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

{{ site.staffersnobio }}

Welcome to DSC 10! Make sure you're familiar with the [Syllabus](../syllabus). The Zoom link to join all course events can be found below.

[Zoom Link](https://ucsd.zoom.us/j/96971704832){: .btn .btn-blue } [Recordings](https://www.youtube.com/playlist?list=PLDNbnocpJUhZDpPKmmbgXAuZqYYPhC0D-){: .btn .btn-green }

{% for module in site.modules %}
{{ module }}
{% endfor %}
