export interface NavigationItem {
  id: string;
  title: string;
  type: 'item' | 'collapse' | 'group';
  translate?: string;
  icon?: string;
  hidden?: boolean;
  url?: string;
  classes?: string;
  groupClasses?: string;
  exactMatch?: boolean;
  external?: boolean;
  target?: boolean;
  breadcrumbs?: boolean;
  children?: NavigationItem[];
  link?: string;
  description?: string;
}

export const NavigationItems: NavigationItem[] = [
  {
    id: 'dashboard',
    title: '',
    type: 'group',
    icon: 'icon-navigation',
    children: [
      {
        id: 'default',
        title: 'Home',
        type: 'item',
        classes: 'nav-item',
        url: '/home',
        icon: 'ti ti-dashboard',
        breadcrumbs: false
      },
      {
        id: 'tabler',
       title: 'My Mentors',
        type: 'item',
        classes: 'nav-item',
        url: '/my-mentors',
        icon: 'ti ti-leaf'
      },
      {
        id: 'breadcrumb',
        title: 'My Mentees',
        type: 'item',
        classes: 'nav-item',
        url: '/my-mentees',
        icon: 'ti ti-hierarchy-2'
      },
      {
        id: 'breadcrumb',
        title: 'My Feedbacks',
        type: 'item',
        classes: 'nav-item',
        url: '/feedback',
        icon: 'ti ti-messages'
      },
      {
        id: 'breadcrumb',
        title: 'My Peers',
        type: 'item',
        classes: 'nav-item',
        url: '/peers',
        icon: 'ti ti-brand-chrome'
      },
      {
        id: 'breadcrumb',
        title: 'Workplace Simulations',
        type: 'item',
        classes: 'nav-item',
        url: '/simulations',
        icon: 'ti ti-brand-android'
      }
    ]
  },
  {
    id: 'authentication',
    title: 'Authentication',
    type: 'group',
    icon: 'icon-navigation',
    children: [
      {
        id: 'login',
        title: 'Login',
        type: 'item',
        classes: 'nav-item',
        url: '/login',
        icon: 'ti ti-login',
        target: true,
        breadcrumbs: false
      },
      {
        id: 'register',
        title: 'Register',
        type: 'item',
        classes: 'nav-item',
        url: '/register',
        icon: 'ti ti-user-plus',
        target: true,
        breadcrumbs: false
      }
    ]
  },
  // {
  //   id: 'other',
  //   title: 'Other',
  //   type: 'group',
  //   icon: 'icon-navigation',
  //   children: [
  //     {
  //       id: 'sample-page',
  //       title: 'Sample Page',
  //       type: 'item',
  //       url: '/sample-page',
  //       classes: 'nav-item',
  //       icon: 'ti ti-brand-chrome'
  //     }
  //   ]
  // }
];
