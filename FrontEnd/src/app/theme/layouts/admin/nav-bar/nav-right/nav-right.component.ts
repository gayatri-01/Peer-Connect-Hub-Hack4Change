// angular import
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/demo/services/api.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-nav-right',
  templateUrl: './nav-right.component.html',
  styleUrls: ['./nav-right.component.scss']
})
export class NavRightComponent implements OnInit {
  constructor(
    private apiService: ApiService,
    private router: Router,
    private toastr: ToastrService
  ) {}

  isLoggedIn: boolean = false;
  firstName: string = '';
  lastName: string = '';
  company: string = '';
  jobTitle: string = '';
  university: string = '';
  degree: string = '';

  ngOnInit(): void {
    this.apiService.isLoggedIn().subscribe(
      (res) => {
        if (res.success === true) {
          this.isLoggedIn = true;
          this.apiService.getUserProfile().subscribe(
            (res) => {
              const details = JSON.parse(res.user_details);
              this.firstName = details.UserInformation.firstName;
              this.lastName = details.UserInformation.lastName;
              this.company = details.UserInformation.company;
              this.jobTitle = details.UserInformation.jobTitle;
              this.university = details.UserInformation.university;
              this.degree = details.UserInformation.degree;
            },
            (err) => {}
          );
        }
      },
      (err) => {}
    );
  }

  // public method
  profile = [
    {
      icon: 'ti ti-user',
      title: 'View Profile',
      url: '/profile'
    },
    {
      icon: 'ti ti-power',
      title: 'Logout',
      url: '/logout'
    }
  ];

  setting = [
    {
      icon: 'ti ti-help',
      title: 'Support'
    },
    {
      icon: 'ti ti-messages',
      title: 'Feedback'
    }
  ];

  logout(): void {
    this.apiService.logout().subscribe((res) => {
      this.toastr.success('You are now logged out.', 'Success');
      this.router.navigate(['/']);
    });
  }
}
