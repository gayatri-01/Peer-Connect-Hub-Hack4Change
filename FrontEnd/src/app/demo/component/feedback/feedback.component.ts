import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { NgxSpinnerModule, NgxSpinnerService } from 'ngx-spinner';

@Component({
  selector: 'app-feedback',
  standalone: true,
  imports: [CommonModule, NgxSpinnerModule],
  templateUrl: './feedback.component.html',
  styleUrl: './feedback.component.scss'
})
export class FeedbackComponent {
  events: any[] = [];
  canLoad = false;

  constructor(private spinner: NgxSpinnerService) {}

  ngOnInit(): void {
    // Sample events data
    this.events = [
      { date: '2024-01-01', description: 'Event 1 description' },
      { date: '2024-02-15', description: 'Event 2 description' },
      { date: '2024-03-10', description: 'Event 3 description' }
      // Add more events as needed
    ];
    this.spinner.show();
    setTimeout(() => {
      this.canLoad = true;
      this.spinner.hide();
    }, 5000);
  }
}
