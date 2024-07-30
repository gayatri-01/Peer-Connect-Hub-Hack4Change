import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
//https://peerconnecthubflask.onrender.com
@Injectable({
  providedIn: 'root'
})
export class ApiService {
  constructor(private http: HttpClient) {}

  register(data): Observable<any> {
    return this.http.post<any>('https://peerconnecthubflask.onrender.com/register', data, { withCredentials: true });
  }

  login(data): Observable<any> {
    return this.http.post('https://peerconnecthubflask.onrender.com/login', data, { withCredentials: true });
  }

  logout(): Observable<any> {
    return this.http.post('https://peerconnecthubflask.onrender.com/logout', {}, { withCredentials: true });
  }

  findMyMentors(): Observable<any> {
    return this.http.get<any>('https://peerconnecthubflask.onrender.com/findMyMentors', { withCredentials: true });
  }

  isLoggedIn(): Observable<any> {
    return this.http.get<any>('https://peerconnecthubflask.onrender.com/isLoggedIn', { withCredentials: true });
  }

  getUserProfile(): Observable<any> {
    return this.http.get<any>('https://peerconnecthubflask.onrender.com/getUserProfile', { withCredentials: true });
  }

  updateUserProfile(data): Observable<any> {
    return this.http.post<any>('https://peerconnecthubflask.onrender.com/updateUserProfile', data, { withCredentials: true });
  }
}
