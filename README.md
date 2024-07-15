# Data-structure-and-algorithm<br>

Question1 : <br>
NCC là công ty công nghệ sinh học cao cấp. Họ vừa phát triển thành công kỹ thuật nhân bản tế bào.<br>
• Để thực hiện được kỹ thuật này, các tế bào được xếp thành 1 hàng ngang theo thứ tự từ trái qua phải (đánh chỉ số từ 1)<br>
• Ban đầu - tức là giây thứ 1, chỉ có 1 tế bào duy nhất kí hiệu là X<br>
• Tại các giây tiếp theo, các tế bào bắt đầu nhân bản theo quy luật:<br>
• Tế bào X nhân bản thành 2 tế bào X và Y (từ trái qua phải)<br>
• Tế bào Y nhân bản thành 2 tế bào Y và X (từ trái qua phải)<br>
Ví dụ<br>
• Giây thứ 1: X<br>
• Giây thứ 2: X Y<br>
• Giây thứ 3: XY YX<br>
Để đảm bảo làm chủ được công nghệ này, công ty muốn tìm ra cách xác định xem tại một thời điểm bất kỳ n₁ nào đó và ở vị trí kị thì tế bào mang kí hiệu gì. Hãy giúp công ty NCC xác định được để làm chủ được công nghệ nhé.<br>
Dữ liệu<br>
• Dòng đầu tiên chứa số nguyên T (1 ≤ T ≤ 10)<br>
• T dòng tiếp theo, dòng thứ i, chứa cặp số nguyên n₁ và kị lần lượt là thời điểm và vị trí mà công ty muốn xác định tế bào. (1 ≤ n ≤ 30, 1 ≤ k ≤ 2n-1)
Kết quả<br>
• In ra T dòng là T kết quả.<br>
<br>
Question2:<br>
Máy tính ở văn phòng Hà Nội thường xuyên xảy ra các sự cố về internet, và Thiết được anh Nhàn phân công nhiệm vụ giải quyết vấn đề này.<br>
Hiện trạng văn phòng Hà Nội thì đang có N máy tính (đánh thứ tự từ 0 đến N-1), và được kết nối với nhau thông qua M đường dây cáp, đường dây cáp thứ i sẽ quy định rõ cặp máy tính Ui và Vì được kết nối với nhau.
Khái niệm cần lưu ý: “Hai máy tính được coi là được liên kết với nhau, khi chúng được kết nối trực tiếp với nhau thông qua 1 đường dây, hoặc kết nối gián tiếp qua đường dây của các máy khác”.
Ví dụ: Máy có 2 đường dây kết nối cặp máy (0, 1) và (1,2) thì máy 3 máy 0,1,2 được liên kết với nhau trong đó máy 0 và máy 2 được kết nối gián tiếp với nhau.
Sau khi kiểm tra 1 lượt, Thiết phát hiện ra vấn đề là do các máy tính ở văn phòng đang liên kết không hợp lý: tất cả máy tính ở văn phòng cần phải được liên kết với nhau bất kể trực tiếp hay gián tiếp.
Anh Nhàn vốn là người tính toán kĩ lưỡng không muốn chưa suy nghĩ mà đã bỏ tiền mua đường dây cáp mới luôn. Anh Nhàn muốn Thiết tái sử dụng M đường dây cáp hiện có, Thiết cần tháo một số đường dây cáp đang có ra và kết nối vào một cặp máy tính khác sao cho tất cả các máy tính được liên kết với nhau.
Hãy viết một chương trình tìm số đường dây cáp tối thiểu mà Thiết phải tháo ra kết nối lại cặp máy tính khác sao cho tất cả các máy tính được liên kết với nhau. Nếu không có các nào thì trả về -1 để Thiết báo với anh Nhàn xin tiền mua thêm đường dây cáp mới.<br>
Dữ liệu<br>
• Dòng thứ nhất gồm 2 số nguyên N và M, N ≤ 5*105 và M ≤ 106 và M ≤ N * (N-1)/2<br>
M dòng tiếp theo, dòng thứ i là cặp số Ui và Vì mô tả đường dây cáp thứ i (0 ≤ i ≤ N-1, 0 ≤ Vi≤ N-1, Ui ≠ Vi)<br>
Dữ liệu đảm bảo không có cặp dây cáp (u,v) nào lặp lại.<br>
Kết quả<br>
In ra 1 số nguyên duy nhất là số đường dây cáp tối thiểu mà Thiết cần thay đổi.<br>
Ví dụ<br>
Input 1<br>
4 3<br>
1<br>
0 1<br>
0 2<br>
1 2<br>
Output: 1<br>
Giải thích: Thiết cần di chuyến đường dây (0,1) để kế nối thêm giữa máy tính 0 và 3<br>

Question3:<br>
Anh Nhàn là giám đốc một công ty hàng đầu về công nghệ. Mỗi năm đều nhận được rất nhiều các dự án từ nước ngoài. Nửa cuối của năm 2023 cũng ngoại lệ, công ty đã nhận được thông tin của N dự án tiềm năng, dự án thứ i sẽ mang về lợi nhuận là vị.<br>
Tuy nhiên, Vì các vấn đề về nhân lực và quản lý nên công ty không được chọn quá K dự án liên tiếp (theo đúng thứ tự của đã cho).<br>
Ví dụ: K=2 và thông tin các dự án lần lượt là 8,6,2,5,7 thì công ty không thể chọn liên tiếp 3 dự án (8,6,2), (6,2,5), (2,5,7) để làm; hoặc 4 dự án liên tiếp là (8,6,2,5), ... phương án tốt nhất là bỏ dự án có lợi nhuận là 2 đi, cụ thể như sau: làm liên tiếp 2 dự án (8,6), bỏ dự án (2), làm liên tiếp 2 dự án (5,7);<br>
Hãy giúp anh Nhàn tìm ra phương án chọn các dự án trong N dự án đã cho để đem lại lợi nhuận lớn nhất về cho công ty nhé. Để cho đơn giản, bạn chỉ cần đưa ra con số lợi nhuận tốt nhất có thể đạt được.<br>
Dữ liệu<br>
• Dòng đầu tiên là hai số N và K, trong đó N ≤ 105, K ≤ N<br>
N dòng tiếp theo, dòng thứ i chứa một số nguyên duy nhất vị là lợi nhuận sau khi chọn dự án thứ i, trong đó vì ≤ 2* 109<br>
Kết quả<br>
In ra một số nguyên duy nhất là lợi nhuận lớn nhất có thể được.<br>
Ví dụ<br>
Input<br>
5 2<br>
8<br>
6<br>
2<br>
5<br>
7<br>
Output<br>
26<br>

Question4: <br>
Anh Nhàn có 1 mảnh đất kích thước N dòng x M cột.<br>
Ô ở dòng i và cột j là Ai có giá trị 0 hoặc 1:<br>
• Ajj = 0 thì đó là ô đất xấu, không thể trồng trọt cây nào cũng không làm được gì cả.<br>
• Ajj = 1 thì đó là ô đất tốt muốn trồng cây gì cũng được.<br>
Anh Nhàn muốn chọn một phần đất hình chữ nhật để làm vườn sao cho tất cả các ô của phần đất đó đều là ô đất tốt. Hãy tìm ra phương án có diện tích tốt nhất giúp anh Nhàn nhé.<br>
Để cho đơn giản bạn chỉ cần tìm ra diện tích lớn nhất có thể có là được.<br>
Dữ liệu<br>
• Dòng đầu tiên chứa 2 số nguyên N và M (1 ≤ N, M ≤ 2000)<br>
• N dòng tiếp theo, mỗi dòng chứa M số nguyên 0 hoặc 1.<br>
Kết quả<br>
• 1 số nguyên duy nhất là diện tích của phương án tốt nhất nên làm vườn.<br>
Ví dụ<br>
Input<br>
4 5<br>
1 0 1 0 0<br>
1 0 1 1 1<br>
1 1 1 1 1<br>
1 0 0 1 0<br>
Output: 6<br>
6<br>

Question5:<br>
Để sắp tới đón tiếp đoàn đại biểu cấp cao, thành phố NCC quyết định trồng N cây hoa dọc theo 1 con đường để trang trí. Tuy nhiên, chủ tịch thành phố khá khó tính, ông muốn trồng hoa phải thỏa mãn các điều kiện sau:<br>
• Các cây hoa phải thuộc 5 loại hoa: Hồng, Ly, Mai, Lan và Tulip.<br>
• Vị trí đầu tiên bạn có thể trồng loại hoa nào cũng được.<br>
• Tại các vị trí tiếp theo:<br>
• Hoa Hồng chỉ được trồng liền ngay sau hoa Ly.<br>
• Hoa Ly chỉ được trồng liền ngay sau hoa Hồng hoặc hoa Mai.<br>
• Hoa Mai không được trồng liên ngay sau hoa Mai.<br>
• Hoa Lan chỉ được trồng liền ngay sau hoa Mai hoặc hoa Tulip.<br>
• Hoa Tulip chỉ được trồng liên ngay sau hoa Hồng.<br>
Hãy đếm xem có bao nhiêu cách trồng N cây hoa này dọc trên con đường và thỏa mãn yêu cầu trên. Vì số cách là rất lớn nên chỉ cần trả về kết quả sau khi đã mod cho 10**9 + 7.<br>
Dữ liệu<br>
• 1 số nguyên N duy nhất (1 ≤ N ≤ 1012) là số hoa<br>
Kết quả<br>
• 1 số nguyên duy nhất là kết quả số cách xếp N cây hoa có thể có sau khi đã mod cho 10**9 + 7.<br>
Input: 5<br>
Output: 68<br>

Question6:<br>
Vượt qua bao khó khăn, cuối cùng Mario cũng đến được thử thách cuối cùng để giải cứu công chúa. Cũng giống như trong trò chơi kinh điển Mario phải tiêu diệt quỷ dữ để giải cứu công chúa.
Nếu như thông thường thì anh sẽ chặt đứt cây cầu để diệt được quỷ, nhưng lần này thì hơi khác 1 chút: anh sẽ phải chơi với nó 1 trò chơi và nếu chơi thắng thì công chúa mới được thả ra.
Luật chơi như sau:<br>
• Ban đầu có n đồng tiền vàng.<br>
• Tại một lượt chơi, người chơi ở lượt đó có quyền lấy đi 1, 2 hoặc 3 đồng tiền vàng.<br>
• Mario và quỷ dữ sẽ chơi luân phiên nhau, nhưng Mario luôn là người đi trước.<br>
• Người chơi thắng cuộc là người lấy đi những đồng tiền vàng cuối cùng, vì khi đó sẽ khiến cho người chơi ở lượt tiếp theo không thể tiếp tục nữa, trò chơi kết thúc.<br>
Sau một thời gian suy nghĩ, Mario phát hiện ra trò chơi này có cách chơi tối ưu, tức là trong 1 vài trường hợp Mario luôn có thể chiến thắng. Tuy nhiên, vì quỷ dữ là người nghĩ ra trò này nên nó cũng biết cách chơi tối ưu, nên trong 1 vài trường hợp cho dù Mario đi kiểu gì cũng nó cũng có thể làm cho Mario thua.<br>
Mario phải đấu với quỷ dữ T ván, hãy tính toán xem tại mỗi ván đấu Mario sẽ thắng hay sẽ thua, biết rằng cả 2 đều chơi theo cách tối ưu.<br>
Dữ liệu<br>
• Dòng đầu tiên chứa số nguyên T (1 ≤ T ≤ 20) là số ván đấu.<br>
• T dòng tiếp theo, dòng thứ i chứa số nguyên n₁, số thứ i là số đồng tiền vàng ở ván đấu thứ i. (1 ≤ n ≤ 109)<br>
Kết quả<br>
• In ra T dòng, dòng thứ i gồm số kết quả của ván đấu thứ i, true nếu Mario thắng, false nếu quỷ dữ thắng.<br>
Input<br>
3<br>
1<br>
2<br>
4<br>
Output<br>
True<br>
True<br>
False<br>
