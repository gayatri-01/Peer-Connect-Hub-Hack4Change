import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
//http://127.0.0.1:5000
@Injectable({
  providedIn: 'root'
})
export class ApiService {
  constructor(private http: HttpClient) {}

  register(data): Observable<any> {
    return this.http.post<any>('http://127.0.0.1:5000/register', data, { withCredentials: true });
  }

  login(data): Observable<any> {
    return this.http.post('http://127.0.0.1:5000/login', data, { withCredentials: true });
  }

  logout(): Observable<any> {
    return this.http.post('http://127.0.0.1:5000/logout', {}, { withCredentials: true });
  }

  findMyMentors(): Observable<any> {
    return this.http.get<any>('http://127.0.0.1:5000/findMyMentors', { withCredentials: true });
  }

  isLoggedIn(): Observable<any> {
    return this.http.get<any>('http://127.0.0.1:5000/isLoggedIn', { withCredentials: true });
  }

  getUserProfile(): Observable<any> {
    return this.http.get<any>('http://127.0.0.1:5000/getUserProfile', { withCredentials: true });
  }

  updateUserProfile(data): Observable<any> {
    return this.http.post<any>('http://127.0.0.1:5000/updateUserProfile', data, { withCredentials: true });
  }
}
