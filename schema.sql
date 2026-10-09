<code>CREATE TABLE IF NOT EXISTS public.content_jobs (
id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
telegram_user_id TEXT,
topic TEXT NOT NULL,
status TEXT NOT NULL DEFAULT 'pending',
content_package JSONB NOT NULL DEFAULT '{}'::jsonb,
created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_content_jobs_user
ON public.content_jobs (telegram_user_id);

CREATE INDEX IF NOT EXISTS idx_content_jobs_created
ON public.content_jobs (created_at DESC);

ALTER TABLE public.content_jobs ENABLE ROW LEVEL SECURITY;</code>
