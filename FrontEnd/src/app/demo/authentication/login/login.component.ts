// angular import
import { Component, OnInit } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [RouterModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export default class LoginComponent implements OnInit {
  emailAddress: string = '';
  password: string = '';
  
  constructor(
    private apiService: ApiService,
    private router: Router,
    private toastr: ToastrService
  ) {}

  ngOnInit(): void {
    this.apiService.isLoggedIn().subscribe(
      (res) => {
        if (res.success === true) this.router.navigate(['/profile']);
      },
      (err) => {}
    );
  }

  onLoginClick(): void {
    const data: any = {
      emailAddress: this.emailAddress,
      password: this.password
    };

    this.apiService.login(data).subscribe((resp) => {
      if (resp.success === true) {
        this.router.navigate(['/profile']);
      } else {
        this.toastr.error('Some error occurred while login.', 'Error !');
      }
    });
  }

  // public method
  SignInOptions = [
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
