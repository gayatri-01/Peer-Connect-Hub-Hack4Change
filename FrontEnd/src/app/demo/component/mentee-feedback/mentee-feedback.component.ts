// angular import
import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-mentee-feedback',
  standalone: true,
  imports: [RouterModule, FormsModule],
  templateUrl: './mentee-feedback.component.html',
  styleUrls: ['./mentee-feedback.component.scss']
})
export default class MenteeFeedbackComponent implements OnInit {

  
  constructor(
  ) {}

  ngOnInit(): void {
    
  }

}
