#include <bits/stdc++.h>
using namespace std;

struct Rect {
	int x1, y1, x2, y2;
	void read() { cin >> x1 >> y1 >> x2 >> y2; }
	int area() { return (y2 - y1) * (x2 - x1); }  // Area of the rectangle
};

int intersect(Rect p, Rect q) {
	// Calculate overlap in x and y directions
	int xOverlap = max(0, min(p.x2, q.x2) - max(p.x1, q.x1));
	int yOverlap = max(0, min(p.y2, q.y2) - max(p.y1, q.y1));
	return xOverlap * yOverlap;  // Area of intersection
}

int main() {
	freopen("billboard.in", "r", stdin);
	freopen("billboard.out", "w", stdout);

	Rect a, b, t;  // billboards a, b, and the truck
	a.read();
	b.read();
	t.read();

	// Total visible area = area of both billboards minus area covered by truck
	cout << a.area() + b.area() - intersect(a, t) - intersect(b, t) << "\n";
}
