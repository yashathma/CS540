import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms



def get_data_loader(training=True):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    dataset = datasets.FashionMNIST('./data', train=training, download=True, transform=transform)
    batch_size = 64
    shuffle = training

    data_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
    return data_loader




def build_model():
    model = nn.Sequential(
        nn.Flatten(),
        nn.Linear(784, 128),
        nn.ReLU(),
        nn.Linear(128, 64),
        nn.ReLU(),
        nn.Linear(64, 10)
    )
    return model




def train_model(model, train_loader, criterion, T):
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
    model.train()

    for epoch in range(T):
        running_loss = 0.0
        correct = 0
        total = 0

        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        accuracy = 100 * correct / total
        print(f"Train Epoch: {epoch} Accuracy: {correct}/{total} ({accuracy:.2f}%) Loss: {running_loss / len(train_loader)}")
    

def evaluate_model(model, test_loader, criterion, show_loss=False):
    model.eval()
    test_loss = 0.0
    correct = 0
    total = 0
    
    with torch.no_grad():
        for data, labels in test_loader:
            outputs = model(data)
            loss = criterion(outputs, labels)
            test_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    accuracy = 100 * correct / total
    test_loss /= len(test_loader)
    
    if show_loss:
        print(f'Average loss: {test_loss:.4f}')
    print(f'Accuracy: {accuracy:.2f}%')
    


def predict_label(model, test_images, index):
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']
    model.eval()
    with torch.no_grad():
        logits = model(test_images)
        probabilities = F.softmax(logits[index], dim=0)
        top3_prob, top3_class = torch.topk(probabilities, 3)
        
        for i in range(3):
            print(f"{class_names[top3_class[i]]}: {top3_prob[i] * 100:.2f}%")

if __name__ == '__main__':
    train_loader = get_data_loader()
    test_loader = get_data_loader(False)
    model = build_model()
    criterion = nn.CrossEntropyLoss()
    train_model(model, train_loader, criterion, T=5)
    evaluate_model(model, test_loader, criterion, show_loss=True)
