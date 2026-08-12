# PYTHON WEB FRAMEWORKS — DRF / FLASK / FASTAPI
# ==============================================

# Priority:
# P0 = must know
# P1 = important
# P2 = deeper/follow-up

# The goal is to explain request flow, validation, authentication,
# authorization, serialization, database access, errors, and deployment.

# ============================================================
# DRF
# ============================================================

# Q1 [P0] What is Django REST Framework?
# ANSWER:
# A Django toolkit for building Web APIs with serializers, views,
# authentication, permissions, parsers, renderers, throttling, routers, etc.

# Q2 [P0] Django vs DRF?
# ANSWER:
# Django is the broader web framework; DRF adds API-focused capabilities.

# Q3 [P0] What is a serializer?
# ANSWER:
# Converts complex Python/model data to API representations and validates
# incoming data into Python/native data.

# Q4 [P0] Serializer vs ModelSerializer?
# ANSWER:
# Serializer is more explicit. ModelSerializer derives many fields and
# model behavior from a Django model.

# Q5 [P0] What is serializer validation?
# ANSWER:
# Validation checks incoming data before business logic/persistence.

# Q6 [P0] validate_<field>()?
# ANSWER:
# Field-specific validation method.

# Q7 [P0] validate()?
# ANSWER:
# Object-level validation, useful when multiple fields are involved.

# Q8 [P0] create() / update()?
# ANSWER:
# Serializer hooks controlling creation/update of objects after validation.

# Q9 [P0] APIView?
# ANSWER:
# Explicit class-based view with handlers such as get(), post(), etc.

# Q10 [P0] GenericAPIView?
# ANSWER:
# Adds reusable queryset/serializer behavior used by DRF generic views.

# Q11 [P0] ListAPIView?
# ANSWER:
# Generic view for listing objects.

# Q12 [P0] RetrieveAPIView?
# ANSWER:
# Generic view for retrieving one object.

# Q13 [P0] ViewSet?
# ANSWER:
# Groups related resource actions into one class.

# Q14 [P0] ModelViewSet?
# ANSWER:
# Provides common CRUD actions: list, retrieve, create, update,
# partial_update, destroy.

# Q15 [P0] What is a router?
# ANSWER:
# Generates URL patterns for registered ViewSets.

# Q16 [P0] Authentication vs permission?
# ANSWER:
# Authentication = who are you?
# Permission = are you allowed to do this?

# Q17 [P0] What is IsAuthenticated?
# ANSWER:
# A permission requiring an authenticated requester.

# Q18 [P0] What is a custom permission?
# ANSWER:
# A class implementing application-specific authorization rules.

# Q19 [P1] has_permission vs has_object_permission?
# ANSWER:
# The former checks request/view-level permission; the latter checks
# permission for a particular object.

# Q20 [P0] What is JWT authentication?
# ANSWER:
# Token-based authentication using signed JWTs; exact lifecycle depends
# on the implementation.

# Q21 [P0] Access token vs refresh token?
# ANSWER:
# Access tokens are usually short-lived API credentials; refresh tokens
# obtain new access tokens and are usually longer-lived.

# Q22 [P0] What are parsers?
# ANSWER:
# Convert request bodies into request.data.

# Q23 [P0] What are renderers?
# ANSWER:
# Convert response data into the final response representation.

# Q24 [P0] request.data vs request.query_params?
# ANSWER:
# request.data = parsed body.
# request.query_params = URL query-string parameters.

# Q25 [P1] What is pagination?
# ANSWER:
# Splitting large collections into smaller responses.

# Q26 [P0] What is throttling?
# ANSWER:
# Limiting request frequency according to configured policies.

# Q27 [P0] What is select_related?
# ANSWER:
# Uses SQL joins for single-valued relationships such as ForeignKey and
# OneToOne.

# Q28 [P0] What is prefetch_related?
# ANSWER:
# Performs separate queries and combines related results in Python;
# especially useful for collections/many-to-many/reverse relations.

# Q29 [P0] select_related vs prefetch_related?
# ANSWER:
# select_related -> join.
# prefetch_related -> separate query + Python combination.

# Q30 [P0] What is N+1?
# ANSWER:
# One query loads a collection and then one extra query per item loads
# related data.

# Q31 [P0] How do you prevent N+1?
# ANSWER:
# Inspect queries and use select_related/prefetch_related, annotations,
# or query restructuring.

# Q32 [P0] What is get_queryset()?
# ANSWER:
# Method used by generic views to define the queryset, often dynamically
# based on the request.

# Q33 [P1] Why paginate public list endpoints?
# ANSWER:
# To control database work, response size, memory, network usage, and
# client processing.

# Q34 [P0] Common REST status codes?
# ANSWER:
# 200 success, 201 created, 204 no content, 400 bad request,
# 401 unauthenticated, 403 forbidden, 404 not found, 409 conflict,
# 429 rate limited, 500 unexpected server error.

# ============================================================
# FLASK
# ============================================================

# Q35 [P0] What is Flask?
# ANSWER:
# A lightweight Python web framework with a small core and WSGI heritage.

# Q36 [P0] What is a Flask route?
# ANSWER:
# Mapping from a URL pattern to a Python view function.

# Q37 [P0] Basic Flask endpoint?
# ANSWER:
#
# from flask import Flask, jsonify
# app = Flask(__name__)
#
# @app.get("/health")
# def health():
#     return jsonify({"status": "ok"})

# Q38 [P0] What is request in Flask?
# ANSWER:
# Provides information about the current HTTP request.

# Q39 [P0] What is jsonify?
# ANSWER:
# Builds a JSON HTTP response.

# Q40 [P0] Application context vs request context?
# ANSWER:
# Application context provides app-level objects such as current_app.
# Request context provides request-specific objects such as request/session.

# Q41 [P1] Why use an application factory?
# ANSWER:
# Better testing, configuration, modularity, and multiple app instances.

# Q42 [P1] What is a Blueprint?
# ANSWER:
# A modular way to organize routes/components.

# Q43 [P1] Flask vs Django?
# ANSWER:
# Flask is lightweight and flexible; Django is batteries-included.
# Choose based on ecosystem, requirements, and team.

# Q44 [P1] What is WSGI?
# ANSWER:
# Interface between Python web apps/frameworks and web servers.

# Q45 [P1] Why deploy Flask behind Gunicorn/Nginx?
# ANSWER:
# Gunicorn runs application workers; Nginx can reverse-proxy and handle
# TLS/static files/connection concerns.

# ============================================================
# FASTAPI
# ============================================================

# Q46 [P0] What is FastAPI?
# ANSWER:
# Modern Python API framework centered on type hints, validation,
# OpenAPI, dependency injection, and ASGI.

# Q47 [P0] What is Pydantic?
# ANSWER:
# Library used for typed data parsing and validation.

# Q48 [P0] Example request model?
# ANSWER:
#
# from pydantic import BaseModel
#
# class UserCreate(BaseModel):
#     name: str
#     age: int

# Q49 [P0] What is Depends?
# ANSWER:
# FastAPI's dependency-injection mechanism for supplying dependencies
# such as DB sessions, auth, or services.

# Q50 [P0] What is ASGI?
# ANSWER:
# Interface designed for asynchronous Python web applications and
# protocols.

# Q51 [P0] WSGI vs ASGI?
# ANSWER:
# WSGI is the traditional synchronous interface.
# ASGI supports asynchronous application patterns.

# Q52 [P0] What is async def endpoint?
# ANSWER:
# A coroutine endpoint that can await asynchronous I/O.

# Q53 [P0] Does async automatically make an API faster?
# ANSWER:
# No. It helps mainly with I/O-bound concurrency. Blocking code can still
# block the event loop.

# Q54 [P1] What happens when blocking code runs inside an async endpoint?
# ANSWER:
# It can block the event loop and reduce concurrency.

# Q55 [P1] FastAPI vs Flask?
# ANSWER:
# FastAPI emphasizes type hints, Pydantic, OpenAPI, DI and ASGI.
# Flask has a smaller core and traditional WSGI architecture.

# Q56 [P1] FastAPI vs DRF?
# ANSWER:
# DRF integrates deeply with Django/ORM/auth ecosystem.
# FastAPI is lighter and strongly centered on type hints, Pydantic,
# dependency injection and ASGI.

# ============================================================
# API DESIGN / SECURITY
# ============================================================

# Q57 [P0] What is middleware?
# ANSWER:
# Code participating in request/response processing for cross-cutting
# concerns such as logging, auth, tracing, headers and errors.

# Q58 [P0] Authentication vs authorization?
# ANSWER:
# Authentication identifies the caller; authorization decides what they
# may do.

# Q59 [P0] What is RBAC?
# ANSWER:
# Permissions are assigned through roles such as admin/manager/user.

# Q60 [P1] What is rate limiting?
# ANSWER:
# Restricting request frequency to protect resources and enforce policy.

# Q61 [P0] What is idempotency?
# ANSWER:
# Repeating an operation with the same idempotency semantics does not
# create unintended additional effects.

# Q62 [P1] Which HTTP methods are generally idempotent?
# ANSWER:
# GET, PUT and DELETE are defined as idempotent by HTTP semantics.
# POST is not idempotent by default.

# Q63 [P0] How do you secure an API?
# ANSWER:
# HTTPS, authentication, authorization, validation, secure token handling,
# rate limits, correct CORS/CSRF strategy, safe errors, logging,
# monitoring and dependency security.

# Q64 [P1] What is CORS?
# ANSWER:
# Browser security mechanism controlling permitted cross-origin requests.

# Q65 [P1] What is CSRF?
# ANSWER:
# Attack where a user's browser is induced to make an unwanted authenticated
# request. Mitigation depends on auth/browser architecture.

# Q66 [P0] How should API errors be designed?
# ANSWER:
# Consistent structured responses and appropriate status codes without
# leaking stack traces/secrets/internal details.

# Q67 [P0] How do you test an API?
# ANSWER:
# Unit tests, integration tests, API/HTTP tests, auth/permission tests,
# validation/error tests, and targeted performance tests.

# Q68 [P1] How do you make APIs observable?
# ANSWER:
# Structured logs, metrics, traces/correlation IDs, latency/error
# monitoring and useful alerts.

# ============================================================
# INTERVIEW SYSTEM QUESTIONS
# ============================================================

# Q69 [P0] Explain a DRF request lifecycle.
# ANSWER:
# HTTP request -> middleware -> URL routing -> DRF view ->
# authentication -> permissions/throttling where configured ->
# parsing -> validation -> business logic/database -> serialization/
# rendering -> response middleware -> client.

# Q70 [P0] Where should business logic live?
# ANSWER:
# Keep complex business logic out of thin HTTP handlers when possible.
# Services/domain modules are common approaches. There is no universal
# architecture.

# Q71 [P0] How would you prevent N+1 in a DRF endpoint?
# ANSWER:
# Inspect queries, then use select_related/prefetch_related, annotations,
# or query restructuring.

# Q72 [P1] How would you handle a slow external API?
# ANSWER:
# Timeouts, bounded retries/backoff when safe, circuit breaking where
# useful, async/background work where appropriate, idempotency and
# observability.

# Q73 [P1] How would you design a large file upload API?
# ANSWER:
# Prefer direct object-storage uploads with signed URLs when appropriate,
# validate metadata/size/type, process asynchronously, and manage cleanup.

# Q74 [P1] How would you version an API?
# ANSWER:
# URL, headers/media types, or compatible evolution. Choose based on
# compatibility and organizational requirements.

# ============================================================
# RAPID FIRE
# ============================================================
# Q75 What is DRF?
# Q76 Serializer vs ModelSerializer?
# Q77 APIView vs GenericAPIView?
# Q78 ViewSet vs ModelViewSet?
# Q79 Authentication vs permission?
# Q80 select_related vs prefetch_related?
# Q81 What is N+1?
# Q82 What is throttling?
# Q83 Flask vs Django?
# Q84 Flask application context vs request context?
# Q85 What is WSGI?
# Q86 What is FastAPI?
# Q87 What is Pydantic?
# Q88 What is Depends?
# Q89 What is ASGI?
# Q90 WSGI vs ASGI?
# Q91 Why does blocking code hurt async?
# Q92 What is idempotency?
# Q93 What is CORS?
# Q94 What is CSRF?
# Q95 What is middleware?
# Q96 How do you secure an API?
