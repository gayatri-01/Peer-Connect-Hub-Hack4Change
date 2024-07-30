import { Component } from '@angular/core';
interface Node {
  id: string;
  label: string;
  class?: string;
  top: number;
  left: number;
}

interface Link {
  source: string;
  target: string;
}

@Component({
  selector: 'app-my-mentees',
  standalone: true,
  imports: [],
  templateUrl: './my-mentees.component.html',
  styleUrl: './my-mentees.component.scss'
})
export default class MyMenteesComponent {
}
