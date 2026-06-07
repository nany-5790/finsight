# Finsight

**Fintech SaaS for Enterprise Operations Management**

Multi-tenant platform designed for companies that need to manage financial transactions, auditing, user roles, and reports under bank-level security standards.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12 + Django 5.0 |
| API | Django REST Framework |
| Authentication | JWT via `djangorestframework-simplejwt` |
| Database (dev) | SQLite |
| Database (prod) | PostgreSQL 16 |
| Filters | `django-filter` |
| Environment variables | `python-decouple` |

---

## Project Architecture

```
finsight/
├── apps/
│   ├── core/           # Abstract base models (TimeStampedModel, SoftDeleteModel)
│   ├── tenants/        # Client companies (multi-tenancy)
│   ├── accounts/       # Users, roles and RBAC
│   ├── transactions/   # Financial accounts and transactions
│   ├── audit/          # Immutable audit logs
│   └── reports/        # Financial reports
├── config/             # Settings, root URLs, WSGI
├── requirements.txt
└── manage.py
```

---

## Modules

### `core`
Abstract base models inherited by all models in the system.

- **`TimeStampedModel`** — provides UUID `id`, `created_at`, `updated_at`, `is_active`
- **`SoftDeleteModel`** — extends `TimeStampedModel` with `deleted_at` and a manager that excludes deleted records. Records are never physically deleted.

### `tenants`
Client company management in a multi-tenant architecture.

- **`Tenant`** — company registered on the platform with `tax_id` (EIN), `domain`, and subscription plan (`free`, `pro`, `enterprise`)

### `accounts`
Users, authentication, and role-based access control (RBAC).

- **`UserProfile`** — extends Django's User with a role (`admin`, `accountant`, `auditor`, `viewer`) and tenant association
- **`AuditUserAction`** — records every `login`, `logout`, and `failed_login` with IP address and user agent

### `transactions`
Financial core of the platform.

- **`Account`** — financial account with `balance` stored as `DecimalField` with bank-level precision (`max_digits=19, decimal_places=4`)
- **`Transaction`** — money movements with `idempotency_key` to prevent duplicate payments and a state machine: `pending` → `processing` → `completed` / `failed` / `cancelled`

### `audit`
Immutable record of all system actions. SOX compliance.

- **`AuditLog`** — records actor, affected model, object, JSON changes, and IP address. The `save()` and `delete()` methods are blocked — no user can modify or delete a log.

### `reports`
Aggregated financial reports by period.

- **`FinancialReport`** — stores `total_credits`, `total_debits`, and `net_balance` by date range with frequencies: `daily`, `weekly`, `monthly`, `annual`

---

## Installation

```bash
# Clone the repository
git clone <repo-url>
cd finsight

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

---

## Design Principles

- **Soft delete** — no financial record is physically deleted
- **UUID as primary key** — unpredictable IDs for enhanced security
- **Decimal instead of float** — exact financial precision following banking standards
- **Idempotency** — transactions cannot be processed twice
- **Audit immutability** — logs cannot be modified even by a superuser
- **Least privilege** — the default role for a new user is `viewer`
- **Multi-tenancy** — each company operates in complete data isolation

---

## Roadmap

- [x] Phase 1 — Base models (`core`)
- [x] Phase 2 — Multi-tenancy (`tenants`)
- [x] Phase 3 — Users and RBAC (`accounts`)
- [x] Phase 4 — Financial transactions (`transactions`)
- [x] Phase 5 — Immutable audit (`audit`)
- [x] Phase 6 — Financial reports (`reports`)
- [ ] Phase 7 — JWT Authentication (login/logout endpoints)
- [ ] Phase 8 — Full REST API with DRF
- [ ] Phase 9 — Automatic audit middleware
- [ ] Phase 10 — Docker + PostgreSQL
- [ ] Phase 11 — CI/CD with GitHub Actions
- [ ] Phase 12 — AWS Deployment (EC2, RDS, S3, IAM, CloudWatch, Secrets Manager)

---

## Author

**Yohani Rodriguez** — Senior Python/Django Backend Developer  
[DracoCode](https://nany-5790.github.io/yohani)
