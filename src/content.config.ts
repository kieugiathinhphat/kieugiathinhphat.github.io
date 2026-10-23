import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const posts = defineCollection({
  loader: glob({ base: './src/content/posts', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    pubDate: z.coerce.date(),
    type: z.enum(['Project', 'Code', 'Notes', 'Journal']).default('Notes'),
    draft: z.boolean().default(false),
  }),
});

export const collections = { posts };
