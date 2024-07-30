// Angular import
import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MyMentorsComponent } from 'src/app/demo/component/my-mentors/my-mentors.component';

@Component({
  selector: 'app-card',
  standalone: true,
  imports: [CommonModule,MyMentorsComponent],
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss']
})
export class CardComponent {
  // public props
  @Input() cardTitle: string;
  @Input() cardClass!: string;
  @Input() blockClass!: string;
  @Input() headerClass!: string;
  @Input() hidHeader: boolean;

  myMentorss : MyMentorsComponent;

  // Constructor
  constructor(private myMentors : MyMentorsComponent) {
    this.hidHeader = false;
    this.cardTitle = 'Card Title';
    this.myMentorss = myMentors;
  }

  findMentors(){
this.myMentorss.findMentors();
  }
}
