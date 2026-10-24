# Workspace

Your standards efforts live here, one folder each:

```
workspace/
  proposal-metadata-standard/
    effort.yaml                          # cycle, phase, node status, baselines, log, open questions
    # Scope and Start
    simple-canvas.yaml  opportunity-frame.yaml  standard-classification.yaml  ecosystem.yaml
    aims-and-objectives.yaml  development.yaml  sustainability-model.yaml
    scope-and-start-bundle.yaml  development-readiness-record.yaml
    # Development
    development-work.yaml  development-outcomes-bundle.yaml
    # Launch and Adoption
    launch.yaml  launch-and-adoption-outcomes.yaml
    # Review and Update
    review.yaml  lifecycle-decision-record.yaml
    scope-bundle.md                      # readable narratives, when you want one to share
    audits/
      2026-10-21-scope-audit.yaml
      2026-10-21-scope-audit.md
```

Ask your agent to *guide* an effort or *audit* one and it will create the folder from `toolkit/templates/`.

Everything in `workspace/` except this README is git-ignored, so your effort's material is not pushed to the framework repository by accident. If you keep your effort in its own fork, delete the `workspace/*` lines from `.gitignore` to version it.
