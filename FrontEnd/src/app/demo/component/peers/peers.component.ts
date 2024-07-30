import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-peers',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './peers.component.html',
  styleUrl: './peers.component.scss'
})
export class PeersComponent {

  filteredStudents: any[] = [];
  searchQuery: string = '';

  students: any[] = [
    { name: 'Aditya Sharma', intro: 'Computer Science student with a passion for coding.', course: 'Computer Science', semester: '3rd' },
    { name: 'Neha Patel', intro: 'Aspiring web developer excited to learn Angular.', course: 'Information Technology', semester: '2nd' },
    { name: 'Rahul Kumar', intro: 'Data science enthusiast with a knack for machine learning.', course: 'Data Science', semester: '4th' },
    { name: 'Pooja Gupta', intro: 'Cybersecurity enthusiast aiming to secure digital environments.', course: 'Cybersecurity', semester: '3rd' },
    { name: 'Aishwarya Singh', intro: 'Passionate about UX design and creating intuitive user interfaces.', course: 'Graphic Design', semester: '2nd' },
    { name: 'Ravi Tiwari', intro: 'Interested in software engineering and building scalable applications.', course: 'Software Engineering', semester: '4th' },
    { name: 'Meera Reddy', intro: 'Eager to explore the world of artificial intelligence and its applications.', course: 'Artificial Intelligence', semester: '3rd' },
    { name: 'Ankit Verma', intro: 'Fascinated by the intersection of technology and business strategy.', course: 'Business Administration', semester: '2nd' },
    { name: 'Priya Joshi', intro: 'Passionate about environmental sustainability and utilizing technology for positive impact.', course: 'Environmental Science', semester: '4th' },
    { name: 'Alok Gupta', intro: 'Aiming to become a full-stack developer proficient in both frontend and backend technologies.', course: 'Computer Engineering', semester: '3rd' },
    // Add more student records as needed
  ];

  ngOnInit(): void {
    this.filteredStudents = this.students;
  }

  searchStudents() {
    this.filteredStudents = this.students.filter(student =>
      student.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
      student.intro.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
      student.course.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
      student.semester.toLowerCase().includes(this.searchQuery.toLowerCase())
    );
  }
}
