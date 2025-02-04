// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://user-dk.github.io/cosmic-notes/',
	integrations: [
		starlight({
			title: 'The Cosmic Notes',
			social: {
				github: 'https://github.com/User-DK',
			},
			sidebar: [
				{
					label: 'Advanced DBMS',
					autogenerate: { directory: 'ads' },
					
				},
				{
					label: 'Cloud Computing',
					autogenerate: { directory: 'cloud-computing' },
				},
			],
		}),
	],
});
