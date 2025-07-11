// main.ts
import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter, withHashLocation } from '@angular/router';
import { App } from './app/app';
import { routes } from './app/app.routes';

bootstrapApplication(App, {
  providers: [
    // Aquí habilitamos hash routing:
    provideRouter(routes, withHashLocation())
  ]
})
  .catch(err => console.error(err));
