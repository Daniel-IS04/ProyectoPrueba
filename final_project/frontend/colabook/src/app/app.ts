import { Component }       from '@angular/core';
import { RouterOutlet }    from '@angular/router';
import { CommonModule }    from '@angular/common';
import { RouterLink, RouterLinkActive } from '@angular/router';
// hola
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <nav style="margin-bottom:1rem">
      <a routerLink="/"    routerLinkActive="active">Home</a> |
      <a routerLink="/about" routerLinkActive="active">About</a>
    </nav>
    <router-outlet></router-outlet>
  `,
})
export class App {}
