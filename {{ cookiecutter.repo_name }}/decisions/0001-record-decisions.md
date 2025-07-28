# 1. Record architecture decisions

Date: {{ cookiecutter.created_date }}

## Status

Accepted

## Context

We need a lightweight approach to recording significant decisions, be they architectural or analytical.

## Decision

We will use Architecture Decision Records (ADRs) as outlined by [Michael Nygard](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions). Additionally, the "Justification" section will be used.

## Justification

ADRs are an effective, lightweight approach for recording decisions that have a long term impact on the project.

The Nygard format is simple and popular, however, it lacks a "Justification" section. Hence, it is added.

## Consequences

Long term decisions affecting the project should have a new ADR (incremented in number) added to source control.
