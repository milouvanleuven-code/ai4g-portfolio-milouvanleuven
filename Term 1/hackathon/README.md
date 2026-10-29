# Hackathon 7 – Eyes on Earth: SlootWacht
**Minor: AI for Good | SDG 15 – Life on Land | 29 October 2026**

---

## 1. Homework & workshop assignments → `homework/`

**What was the assignment?**

The hackathon challenge was to develop an AI-powered object detection solution addressing an environmental problem related to SDG 15. We had to collect and annotate at least 300 images, train an object detection model using Roboflow, evaluate its performance on unseen images, and develop a working application or script that demonstrates its practical use.

The assignment also required documentation of our methodology, technical choices, limitations, ethical considerations, and the potential impact of our solution.

**What did I hand in?**

- A Roboflow object detection dataset containing 308 images.
- A trained or training-in-progress RF-DETR object detection model.
- Python scripts for collecting images from online sources.
- A Streamlit application for analysing uploaded images.
- A README documenting the problem, methodology and ethical considerations.

**What did I find difficult, and how did I solve it?**

The biggest challenge was collecting a sufficiently large and relevant image dataset within the available time.

Finding images of Dutch ditches containing clearly visible floating litter, dense aquatic vegetation or drainage openings proved difficult. Many search results were unsuitable because they showed beaches, rubbish on land, unrelated vegetation or objects that were too small to recognise.

We developed Python scripts to collect candidate images from Wikimedia Commons, Openverse and iNaturalist. However, the first two services repeatedly returned HTTP 429 errors or timed out.

We addressed these problems by implementing alternative searches, saving downloaded images locally, combining image batches and manually reviewing the results in Roboflow.

Another challenge was that automatic annotation was not always accurate. Some images contained no relevant objects, while others were incorrectly labelled. I therefore reviewed the generated annotations and rejected unsuitable images instead of accepting all downloaded material.

The final dataset contained 308 images, exceeding the minimum requirement of 300 by 2.7%.

### Checklist
- [x] Collected at least 300 images
- [x] Created an object detection project in Roboflow
- [x] Defined three detection classes
- [x] Reviewed and filtered candidate images
- [x] Generated a dataset version
- [x] Started model training
- [ ] Confirm final model evaluation and successful application test

---

## 2. Hackathon prototype → `hackathon/`

**Project title:**

SlootWacht – AI-Powered Monitoring of Dutch Ditches

**My pair partner:**

Kadir Guclu 

**Tool we had to use:**

Roboflow for image annotation, object detection training and model evaluation.

Additional tools:
- Python for automated image collection and data processing.
- Streamlit for the user interface.
- Requests and Pillow for image processing and API communication.
- GitHub for project documentation and reproducibility.

**SDG we had to address:**

**SDG 15 – Life on Land**, particularly the protection and restoration of ecosystems and biodiversity.

SlootWacht also contributes indirectly to **SDG 6 – Clean Water and Sanitation**, because it focuses on monitoring visible conditions in freshwater environments.

### What problem does it solve, and for whom?

The Netherlands has an extensive network of ditches, canals and small waterways. These environments support aquatic plants, insects, amphibians and other species, while also contributing to drainage and local water management.

However, Dutch surface-water quality remains a serious environmental challenge.

According to the Dutch Environmental Data Compendium, in 2024:

- Only **1 out of 741 assessed Dutch water bodies (approximately 0.13%)** achieved good overall ecological status under the Water Framework Directive.
- **85%** of assessed water bodies had moderate, poor or bad biological quality.
- Approximately **50%** met the physicochemical quality requirements.

