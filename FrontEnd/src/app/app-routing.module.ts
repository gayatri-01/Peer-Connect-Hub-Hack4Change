// angular import
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

// Project import
import { AdminComponent } from './theme/layouts/admin/admin.component';
import { GuestComponent } from './theme/layouts/guest/guest.component';
import { MyMentorsComponent } from './demo/component/my-mentors/my-mentors.component';
import { ProfileComponent} from './demo/component/profile/profile.component';
import { FeedbackComponent } from './demo/component/feedback/feedback.component';
import { PeersComponent } from './demo/component/peers/peers.component';
import { SimulationComponent } from './demo/component/simulation/simulation.component';
import MenteeFeedbackComponent from './demo/component/mentee-feedback/mentee-feedback.component';

const routes: Routes = [
  {
    path: '',
    component: AdminComponent,
    children: [
      {
        path: '',
        redirectTo: '/home',
        pathMatch: 'full'
      },
      {
        path: 'typography',
        loadComponent: () => import('./demo/ui-component/typography/typography.component')
      },
      {
        path: 'card',
        loadComponent: () => import('./demo/component/card/card.component')
      },
      {
        path: 'my-mentors',
        component: MyMentorsComponent
      },
      {
        path: 'mentee-feedback',
        component: MenteeFeedbackComponent
      },

      
      {
        path: 'simulations',
        component: SimulationComponent
      },
      {
        path: 'profile',
        component: ProfileComponent
      },
      {
        path: 'feedback',
        component: FeedbackComponent
      },
      {
        path: 'peers',
        component: PeersComponent
      },
      {
        path: 'my-mentees',
        loadComponent: () => import('./demo/component/my-mentees/my-mentees.component')
      },
      {
        path: 'home',
        loadComponent: () => import('./demo/component/home/home.component')
      },
      {
        path: 'breadcrumb',
        loadComponent: () => import('./demo/component/breadcrumb/breadcrumb.component')
      },
      {
        path: 'color',
        loadComponent: () => import('./demo/ui-component/ui-color/ui-color.component')
      },
      {
        path: 'sample-page',
        loadComponent: () => import('./demo/other/sample-page/sample-page.component')
      }
    ]
  },
  {
    path: '',
    component: GuestComponent,
    children: [
      {
        path: 'login',
        loadComponent: () => import('./demo/authentication/login/login.component')
      },
      {
        path: 'register',
        loadComponent: () => import('./demo/authentication/register/register.component')
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
