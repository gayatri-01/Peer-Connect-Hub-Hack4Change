import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';
import { SharedModule } from 'src/app/theme/shared/shared.module';
import { MatDialog } from '@angular/material/dialog';
import { ModalComponent } from '../modal/modal.component';
import { NgxSpinnerService } from 'ngx-spinner';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { NgxSpinnerModule } from 'ngx-spinner';

@Component({
  selector: 'app-my-mentors',
  standalone: true,
  imports: [CommonModule, SharedModule, NgxSpinnerModule], // Import CommonModule here
  templateUrl: './my-mentors.component.html',
  styleUrl: './my-mentors.component.scss',
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class MyMentorsComponent {
  constructor(
    private apiService: ApiService,
    public dialog: MatDialog,
    private spinner: NgxSpinnerService
  ) {}

  formData: any = {};
  showMentors = false;

  matchesExplained: any;
  mentors: any;

  findMentors() {
    this.spinner.show();
    this.apiService.findMyMentors().subscribe(
      (resp) => {
        this.matchesExplained = JSON.parse(resp.matches);
        this.mentors = JSON.parse(resp.mentors);
        this.showMentors = true;
        this.spinner.hide();
      },
      (err) => {
        console.error(err); // Handle error
      }
    );
  }

  openModal(buttonNumber: number): void {
    let title = '';
    let content = '';
    console.log("Mentosrs info");
    console.log(this.mentors);
    console.log(this.mentors[buttonNumber]);
    const mentors = this.mentors;

    switch (buttonNumber) {
      case 0:
        content = '1';
        break;
      case 1:
        content = '2';
        break;
      case 2:
        content = '3';
        break;
    }
    const matches = JSON.parse(this.matchesExplained);
    const dialogRef = this.dialog.open(ModalComponent, {
      width: '1000px',
      data: { title, content, matches, mentors},
      hasBackdrop: true // Enable backdrop
    });
  }
}
