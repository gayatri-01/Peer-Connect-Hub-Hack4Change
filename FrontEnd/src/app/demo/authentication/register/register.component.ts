// angular import
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ApiService } from '../../services/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [RouterModule, FormsModule],
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export default class RegisterComponent implements OnInit {
  firstName: string;
  lastName: string;
  emailAddress: string;
  password: string;
  confirmPassword: string;
  jobTitle: string;
  degree: string;
  university: string;
  company: string;

  constructor(
    private apiService: ApiService,
    private router: Router,
    private toastr: ToastrService
  ) {}

  ngOnInit(): void {}

  onCreateAccountClick(): void {
    if (this.password !== this.confirmPassword) {
      this.toastr.error('Passwords do not match.', 'Error !!');
    } else {
      const data: any = {
        firstName: this.firstName,
        lastName: this.lastName,
        emailAddress: this.emailAddress,
        password: this.password,
        company: this.company,
        jobTitle: this.jobTitle,
        university: this.university,
        degree: this.degree
      };
      this.apiService.register(data).subscribe((resp) => {
        console.log(resp.success);
        if (resp.success === true) {
          this.router.navigate(['/profile']);
        } else {
          this.toastr.error('Some error occurred while creating your account.', 'Error !');
        }
      });
    }
  }

  // public method
  SignUpOptions = [
    {
      image: 'assets/images/authentication/google.svg',
      name: 'Google'
    },
    {
      image: 'assets/images/authentication/twitter.svg',
      name: 'Twitter'
    },
    {
      image: 'assets/images/authentication/facebook.svg',
      name: 'Facebook'
    }
  ];
}
