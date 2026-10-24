---
phase: develop
domain:
- documentation
- adoption
- accessibility
role: supporting
status: draft
actors:
- editors
- implementers
- educators
- adopters
produces:
- normative-specification
- tutorials
- how-to-guides
- explanation
- reference-material
- examples
- decision-records
---

## Intent

Create the information environments different audiences need to understand, implement, use, evaluate, and maintain the standard.

---

# Principle: Documentation Is Part of the Interface

A standard is not successfully open merely because its specification is publicly readable.

People must be able to:

- discover it;
    
- understand why it exists;
    
- learn it;
    
- implement it;
    
- look things up;
    
- diagnose problems;
    
- understand its limitations.
    

Documentation is part of the usability surface of the standard.

---
# Pattern: One Source of Normative Truth

Do not allow tutorials, guides, examples, or explanation to silently create new requirements.

If supporting documentation contradicts the normative specification:

> the normative specification wins,

and the documentation defect should be corrected.

---

# Pattern: Documentation Should Test the Standard

Writing documentation is itself a form of testing.

If an editor cannot explain:

- what a feature does;
    
- why it exists;
    
- how someone uses it;
    
- what happens when it fails;
    

the underlying standard may still be insufficiently clear.

---

# Pattern: Generate Where Possible

Where documentation can be reliably derived from canonical artifacts, generate it.

Examples:

- schema field reference;
    
- vocabulary lists;
    
- API tables;
    
- version information.
    

This reduces drift and maintenance burden.
