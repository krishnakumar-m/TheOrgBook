import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BusinessComponent } from 'app/business/business.component';
import { CertComponent } from 'app/cert/cert.component';
import { DashboardComponent } from 'app/dashboard/dashboard.component';
import { RoadmapComponent } from 'app/roadmap/roadmap.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  {
    path: 'home',
    component: DashboardComponent,
    data: {
      breadcrumb: 'Search'
    }
  },
  {
    path: 'business/:recordId',
    component: BusinessComponent,
    data: {
      breadcrumb: 'Organization Info'
    }
  },
  {
    path: 'cert/:recordId',
    component: CertComponent,
    data: {
      breadcrumb: 'Permit and License Info'
    }
  },
  {
    path: 'roadmap',
    component: RoadmapComponent,
    data: {
      breadcrumb: 'Roadmap'
    }
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
