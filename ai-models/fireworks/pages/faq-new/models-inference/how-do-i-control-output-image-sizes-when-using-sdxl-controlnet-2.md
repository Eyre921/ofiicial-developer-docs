---
title: "How do I control output image sizes when using SDXL ControlNet?"
source: https://docs.fireworks.ai/faq-new/models-inference/how-do-i-control-output-image-sizes-when-using-sdxl-controlnet
path: faq-new/models-inference/how-do-i-control-output-image-sizes-when-using-sdxl-controlnet
---

When using **SDXL ControlNet** (e.g., canny control), the output image size is determined by the explicit **width** and **height** parameters in your API request:

The input control signal image will be automatically:

* **Resized** to fit your specified dimensions
* **Cropped** to preserve aspect ratio

**Example**: To generate a 768x1344 image, explicitly include these parameters in your request:

```json theme={null}
{
    "width": 768,
    "height": 1344
}
```

*Note*: While these parameters may not appear in the web interface examples, they are supported API parameters that can be included in your requests.
