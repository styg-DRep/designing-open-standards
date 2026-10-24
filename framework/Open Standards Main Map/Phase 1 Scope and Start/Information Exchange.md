---
phase:
  - scope
  - develop
  - review
domain:
  - interoperability
  - exchange
  - interfaces
role: supporting
status: stable
actors:
  - standards-developers
  - implementers
  - infrastructure-maintainers
  - tool-developers
produces:
  - schemas
  - specifications
  - templates
  - interfaces
  - exchange-rules
  - validation-rules
---

## Intent

Create consistent ways for governance information or governance objects to move between people, organisations, tools, or systems.

Exchange standards become useful when participants agree broadly on what information matters but lack interoperable ways to represent or transfer it.

## Governance-native forms

An exchange standard might specify:

- proposal metadata;
    
- decision records;
    
- voting records;
    
- rationale formats;
    
- governance APIs;
    
- deliberation records;
    
- implementation-status records;
    
- treasury reporting;
    
- identity or delegation information;
    
- machine-readable governance artifacts.
    

## Discovery questions

Ask:

- Does equivalent information exist in incompatible forms?
    
- Are participants repeatedly translating information manually?
    
- Are tools unable to consume one another's outputs?
    
- Is important governance context lost between systems?
    
- Can information be validated consistently?
    
- Are producers and consumers implicitly relying on undocumented formats?
    

## Typical products

- schema
    
- specification
    
- template
    
- API contract
    
- serialization format
    
- validation rules
    
- mapping
    
- interoperability profile
    

## Exchange pattern

A good exchange standard should make explicit:

> **What is exchanged → in what form → according to what rules → between whom → with what validation.**
